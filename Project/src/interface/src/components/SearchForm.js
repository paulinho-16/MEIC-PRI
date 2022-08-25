import React from 'react'
import { Form, InputGroup, FormControl } from 'react-bootstrap'

import SearchBar from './SearchBar'
import SearchButton from './SearchButton'
import Dropdown from 'react-bootstrap/Dropdown'

class SearchForm extends React.Component {
    constructor(props) {
        super(props)
        this.searchTextRef = React.createRef()
        let fields = ['title', 'originCountry', 'language', 'cast', 'genres', 'summary', 'imdbID']
        let types = ['animation', 'miniSeries', 'movie', 'series', 'short', 'special']
        let checked_fields = new Array(fields.length).fill(true)
        let checked_types = new Array(types.length).fill(true)
        this.state = {
            fields: fields,
            types: types,
            checked_fields: checked_fields,
            checked_types: checked_types,
            startYearInitial: null || '',
            startYearFinal: null || '',
            endYearInitial: null || '',
            endYearFinal: null || '',
            numEpisodesInitial: null || '',
            numEpisodesFinal: null || '',
            runtimeInitial: null || '',
            runtimeFinal: null || '',
            ratingInitial: null || '',
            ratingFinal: null || '',
            numVotesInitial: null || '',
            numVotesFinal: null || '',
            sortBy: "relevant"
        };
    }

    handleSearch = () => {
        const searchText = this.searchTextRef.current.value
        const search_fields = this.state.fields.filter((_, index) => this.state.checked_fields[index]);
        const excluded_show_types = this.state.types.filter((_, index) => !this.state.checked_types[index]);
        if (this.state.sortBy === "episodes ASC" || this.state.sortBy === "episodes DESC")
            ['movie', 'animation', 'special', 'short'].forEach((type, index) => excluded_show_types.indexOf(type) === -1 ? excluded_show_types.push(type) : '')

        if (search_fields.length === 0 || excluded_show_types.length === this.state.types.length) {
            this.props.updateResults([])
            return
        }

        let uri = null
        if (searchText === '') {
            uri = '/solr/shows/select?indent=true&q.op=OR&q=*:*'
        }
        else
            uri = '/solr/shows/select?indent=true&q.op=OR'

        if (!(searchText === '')) {
            for (var i = 0; i < search_fields.length; i++) {
                if (i === 0)
                    uri += ` &q=(${search_fields[i]}:"${searchText}"`
                else
                    uri += ` ${search_fields[i]}:"${searchText}"`
            }
            uri += ')'
        }

        let startYearInitial = (this.state.startYearInitial) ? this.state.startYearInitial : '*'
        let startYearFinal = (this.state.startYearFinal) ? this.state.startYearFinal : '*'

        uri += (!this.state.startYearInitial && !this.state.startYearFinal) ? '' : ` AND startYear:[${startYearInitial} TO ${startYearFinal}]`

        let endYearInitial = (this.state.endYearInitial) ? this.state.endYearInitial : '*'
        let endYearFinal = (this.state.endYearFinal) ? this.state.endYearFinal : '*'

        uri += (!this.state.endYearInitial && !this.state.endYearFinal) ? '' : ` AND endYear:[${endYearInitial} TO ${endYearFinal}]`

        let numEpisodesInitial = (this.state.numEpisodesInitial) ? this.state.numEpisodesInitial : '*'
        let numEpisodesFinal = (this.state.numEpisodesFinal) ? this.state.numEpisodesFinal : '*'

        uri += (!this.state.numEpisodesInitial && !this.state.numEpisodesFinal) ? '' : ` AND episodes:[${numEpisodesInitial} TO ${numEpisodesFinal}]`

        let runtimeInitial = (this.state.runtimeInitial) ? this.state.runtimeInitial : '*'
        let runtimeFinal = (this.state.runtimeFinal) ? this.state.runtimeFinal : '*'

        uri += (!this.state.runtimeInitial && !this.state.runtimeFinal) ? '' : ` AND runtime:[${runtimeInitial} TO ${runtimeFinal}]`

        let ratingInitial = (this.state.ratingInitial) ? this.state.ratingInitial : '*'
        let ratingFinal = (this.state.ratingFinal) ? this.state.ratingFinal : '*'

        if ((this.state.ratingInitial) == "*" && (this.state.sortBy === "rating ASC" || this.state.sortBy === "rating DESC"))
            this.state.ratingInitial = 0

        uri += (!this.state.ratingInitial && !this.state.ratingFinal) ? '' : ` AND rating:[${ratingInitial} TO ${ratingFinal}]`

        let numVotesInitial = (this.state.numVotesInitial) ? this.state.numVotesInitial : '*'
        let numVotesFinal = (this.state.numVotesFinal) ? this.state.numVotesFinal : '*'

        uri += (!this.state.numVotesInitial && !this.state.numVotesFinal) ? '' : ` AND numVotes:[${numVotesInitial} TO ${numVotesFinal}]`

        if (excluded_show_types.length != 0) {
            for (var i = 0; i < excluded_show_types.length; i++) {
                if (i === 0)
                    uri += ` AND (NOT type:"${excluded_show_types[i]}"`
                else
                    uri += ` NOT type:"${excluded_show_types[i]}"`
            }
            uri += ')'
        }

        uri += '&rows=100'

        if (this.state.sortBy!=="relevant"){
            uri+=`&sort=${this.state.sortBy}`
        }

        console.log(uri)

        // uri += '&defType=edismax&indent=true&qf=title^4 language^3 popularRank^2 summary^1&debugQuery=true&tie=0.2'

        let uri_encoded = encodeURI(uri);

        uri_encoded = uri_encoded + "&defType=edismax&indent=true&qf=title%5E4%20language%5E3%20popularRank%5E2%20summary%5E1&debugQuery=true&tie=0.2"

        if (searchText !== "") {
            let spell_check_uri = encodeURI(`/solr/shows/spell?q=title:${searchText}&amp;spellcheck=true&amp;spellcheck.count=10`)

            fetch(spell_check_uri).then((data) => {
                data.json().then((resp) => {
                    try {
                        this.props.updateSpellCheck(resp['spellcheck']['suggestions'][1]['suggestion'])
                    }
                    catch {
                        this.props.updateSpellCheck([])
                    }
                })
            })
        }
        else {
            this.props.updateSpellCheck([])
        }

        fetch(uri_encoded).then((data) => {
            data.json().then((resp) => {
                this.props.updateResults(resp['response']['docs'])
            })
        })
    }

    updateInputValue(evt, field) {
        const value = evt.target.value;

        this.setState({
            [field]: value
        });
    }

    sortByUpdate(field) {
        this.setState({
            sortBy: field
        });
    }

    handleFieldsCheckbox = (position) => {
        const updatedCheckedState = this.state.checked_fields.map((item, index) => index === position ? !item : item);
        this.state.checked_fields = updatedCheckedState
    }

    handleTypesCheckbox = (position) => {
        const updatedCheckedState = this.state.checked_types.map((item, index) => index === position ? !item : item);
        this.state.checked_types = updatedCheckedState
    }

    render() {
        return (
            <Form className="search-form">
                <div className="sortBy">
                    <div className="sortByChild1">
                        <SearchBar ref={this.searchTextRef} />
                    </div>
                    <div className="sortByChild2">
                        <Dropdown>
                            <Dropdown.Toggle variant="danger" id="dropdown-basic">
                                Sort By: {this.state.sortBy}
                            </Dropdown.Toggle>

                            <Dropdown.Menu>
                                <Dropdown.Item onClick={() => this.sortByUpdate("relevant") }>Relevant</Dropdown.Item>
                                <Dropdown.Item onClick={() => this.sortByUpdate("rating ASC")}>Rating ASC</Dropdown.Item>
                                <Dropdown.Item onClick={() => this.sortByUpdate("rating DESC")}>Rating DESC</Dropdown.Item>
                                <Dropdown.Item onClick={() => this.sortByUpdate("episodes ASC")}>Episodes ASC</Dropdown.Item>
                                <Dropdown.Item onClick={() => this.sortByUpdate("episodes DESC")}>Episodes DESC</Dropdown.Item>
                                <Dropdown.Item onClick={() => this.sortByUpdate("numVotes ASC")}>Number of Votes ASC</Dropdown.Item>
                                <Dropdown.Item onClick={() => this.sortByUpdate("numVotes DESC")}>Number of Votes DESC</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>
                    </div>
                </div>
                <Form.Group className="search-filters" controlId="searchFilters">
                    <Form.Group className="type-checkboxes" controlId="fieldsSearch">
                        <Form.Label>Search Fields:</Form.Label>
                        {this.state.fields.map((field, index) => (
                            <div key={field}>
                                <input
                                    type="checkbox"
                                    name="searchFields"
                                    value={`${field}`}
                                    defaultChecked={this.state.checked_fields[index]}
                                    onChange={() => this.handleFieldsCheckbox(index)}
                                /> {`${field}`}
                            </div>
                        ))}
                    </Form.Group>

                    <Form.Group className="type-checkboxes" controlId="typesSearch">
                        <Form.Label>Show Type:</Form.Label>
                        {this.state.types.map((type, index) => (
                            <div key={type}>
                                <input
                                    type="checkbox"
                                    name="showTypes"
                                    value={`${type}`}
                                    defaultChecked={this.state.checked_types[index]}
                                    onChange={() => this.handleTypesCheckbox(index)}
                                /> {`${type}`}
                            </div>
                        ))}
                    </Form.Group>

                    <Form.Group className="input-years" controlId="yearsSearch">
                        <div>
                            <Form.Label>Start Year:</Form.Label>
                            <div>
                                <input value={this.state.startYearInitial} onChange={evt => this.updateInputValue(evt, "startYearInitial")} type="number" min={0} max={3000} style={{ marginRight: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input value={this.state.startYearFinal} onChange={evt => this.updateInputValue(evt, "startYearFinal")} type="number" min={0} max={3000} style={{ marginLeft: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>End Year:</Form.Label>
                            <div>
                                <input type="number" value={this.state.endYearInitial} onChange={evt => this.updateInputValue(evt, "endYearInitial")} min={0} max={3000} style={{ marginRight: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.endYearFinal} onChange={evt => this.updateInputValue(evt, "endYearFinal")} min={0} max={3000} style={{ marginLeft: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>
                    </Form.Group>

                    <Form.Group className="input-episodes-runtime" controlId="episodesRuntimeSearch">
                        <div>
                            <Form.Label>Number of Episodes:</Form.Label>
                            <div>
                                <input type="number" value={this.state.numEpisodesInitial} onChange={evt => this.updateInputValue(evt, "numEpisodesInitial")} min={0} max={10000} style={{ marginRight: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.numEpisodesFinal} onChange={evt => this.updateInputValue(evt, "numEpisodesFinal")} min={0} max={10000} style={{ marginLeft: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>Runtime:</Form.Label>
                            <div>
                                <input type="number" value={this.state.runtimeInitial} onChange={evt => this.updateInputValue(evt, "runtimeInitial")} min={0} max={10000} style={{ marginRight: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.runtimeFinal} onChange={evt => this.updateInputValue(evt, "runtimeFinal")} min={0} max={10000} style={{ marginLeft: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>
                    </Form.Group>

                    <Form.Group className="input-rating-votes" controlId="ratingNumVotesSearch">
                        <div>
                            <Form.Label>Rating:</Form.Label>
                            <div>
                                <input type="number" value={this.state.ratingInitial} onChange={evt => this.updateInputValue(evt, "ratingInitial")} min={0} max={10} step={0.1} style={{ marginRight: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.ratingFinal} onChange={evt => this.updateInputValue(evt, "ratingFinal")} min={0} max={10} step={0.1} style={{ marginLeft: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>Number of Votes:</Form.Label>
                            <div>
                                <input type="number" value={this.state.numVotesInitial} onChange={evt => this.updateInputValue(evt, "numVotesInitial")} min={0} max={2000000} style={{ marginRight: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.numVotesFinal} onChange={evt => this.updateInputValue(evt, "numVotesFinal")} min={0} max={2000000} style={{ marginLeft: '1rem' }} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>
                    </Form.Group>
                </Form.Group>

                <SearchButton handleFunction={this.handleSearch} />
            </Form >
        )
    }
}

export default SearchForm
