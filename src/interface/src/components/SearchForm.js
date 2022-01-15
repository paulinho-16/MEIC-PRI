import React from 'react'
import { Form, InputGroup, FormControl } from 'react-bootstrap'

import SearchBar from './SearchBar'
import SearchButton from './SearchButton'

class SearchForm extends React.Component {
    constructor(props) {
        super(props)
        this.searchTextRef = React.createRef()
        let types = ['animation', 'miniSeries', 'movie', 'series', 'short', 'special']
        let checked = new Array(types.length).fill(true)
        this.state = {
            types: types,
            checked: checked,
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
            numVotesFinal: null || ''
        };
    }

    updateInputValue(evt, field) {
        const val = evt.target.value;

        if (field === "startYearInitial"){
            this.setState({
                startYearInitial: val
            });
        }
        if (field === "startYearFinal"){
            this.setState({
                startYearFinal: val
            });
        }
        if (field === "endYearInitial"){
            this.setState({
                endYearInitial: val
            });
        }
        if (field === "endYearFinal"){
            this.setState({
                endYearFinal: val
            });
        }
        if (field === "numEpisodesInitial"){
            this.setState({
                numEpisodesInitial: val
            });
        }
        if (field === "numEpisodesFinal"){
            this.setState({
                numEpisodesFinal: val
            });
        }
        if (field === "runtimeInitial"){
            this.setState({
                runtimeInitial: val
            });
        }
        if (field === "runtimeFinal"){
            this.setState({
                runtimeFinal: val
            });
        }

        if (field === "ratingInitial"){
            this.setState({
                ratingInitial: val
            });
        }
        if (field === "ratingFinal"){
            this.setState({
                ratingFinal: val
            });
        }
        
        if (field === "numVotesInitial"){
            this.setState({
                numVotesInitial: val
            });
        }
        if (field === "numVotesFinal"){
            this.setState({
                numVotesFinal: val
            });
        }
        
        console.log(this.state.startYearInitial)
    }

    handleSearch = () => {
        const searchText = this.searchTextRef.current.value        
        const show_types = this.state.types.filter((_, index) => this.state.checked[index]);

        if (show_types.length === 0) {
            this.props.updateResults([])
            return
        }

        let uri = null
        if (searchText === '') // TODO: recolher apenas alguns de todos os resultados (paginação?)
            uri = '/solr/shows/select?indent=true&q.op=OR&q=*:*'
        else
            uri = `/solr/shows/select?indent=true&q.op=OR&q=(title:"${searchText}" language:"${searchText}" summary:"${searchText}")` // TODO: language:"${searchText}" summary:"${searchText}" 

        if (this.state.startYearInitial > 0 & this.state.startYearFinal >0 )
        {
            uri = uri + ` AND startYear:[${this.state.startYearInitial} TO ${this.state.startYearFinal}]`
        }
        else if (this.state.startYearInitial > 0)
        {
            uri = uri + ` AND startYear:[${this.state.startYearInitial} TO 3000]`
        }
        else if (this.state.startYearFinal > 0 )
        {
            uri = uri + ` AND startYear:[1 TO ${this.state.startYearFinal}]`
        }

        if (this.state.endYearInitial > 0 & this.state.endYearFinal >0 )
        {
            uri = uri + ` AND endYear:[${this.state.endYearInitial} TO ${this.state.endYearFinal}]`
        }
        else if (this.state.endYearInitial > 0)
        {
            uri = uri + ` AND endYear:[${this.state.endYearInitial} TO 3000]`
        }
        else if (this.state.endYearFinal > 0 )
        {
            uri = uri + ` AND endYear:[1 TO ${this.state.endYearFinal}]`
        }

        if (this.state.numEpisodesInitial > 0 & this.state.numEpisodesFinal >0 )
        {
            uri = uri + ` AND episodes:[${this.state.numEpisodesInitial} TO ${this.state.numEpisodesFinal}]`
        }
        else if (this.state.numEpisodesInitial > 0)
        {
            uri = uri + ` AND episodes:[${this.state.numEpisodesInitial} TO 10000]`
        }
        else if (this.state.numEpisodesFinal > 0 )
        {
            uri = uri + ` AND episodes:[1 TO ${this.state.numEpisodesFinal}]`
        }

        if (this.state.runtimeInitial > 0 & this.state.runtimeFinal > 0 )
        {
            uri = uri + ` AND runtime:[${this.state.runtimeInitial} TO ${this.state.runtimeFinal}]`
        }
        else if (this.state.runtimeInitial > 0)
        {
            uri = uri + ` AND runtime:[${this.state.runtimeInitial} TO 10000]`
        }
        else if (this.state.runtimeFinal > 0 )
        {
            uri = uri + ` AND runtime:[0 TO ${this.state.runtimeFinal}]`
        }

        if (this.state.ratingInitial > 0.0 & this.state.ratingFinal > 0.0 )
        {
            uri = uri + ` AND rating:[${this.state.ratingInitial} TO ${this.state.ratingFinal}]`
        }
        else if (this.state.ratingInitial > 0.0)
        {
            uri = uri + ` AND rating:[${this.state.ratingInitial} TO 10]`
        }
        else if (this.state.ratingFinal > 0.0 )
        {
            uri = uri + ` AND rating:[0 TO ${this.state.ratingFinal}]`
        }

        if (this.state.numVotesInitial > 0.0 & this.state.numVotesFinal > 0.0 )
        {
            uri = uri + ` AND numVotes:[${this.state.numVotesInitial} TO ${this.state.numVotesFinal}]`
        }
        else if (this.state.numVotesInitial > 0.0)
        {
            uri = uri + ` AND numVotes:[${this.state.numVotesInitial} TO 1000000]`
        }
        else if (this.state.numVotesFinal > 0.0 )
        {
            uri = uri + ` AND numVotes:[0 TO ${this.state.numVotesFinal}]`
        } 
  
        for (var i = 0; i < show_types.length; i++) {
            if (i === 0)
                uri += ` AND (type:"${show_types[i]}"`
            else
                uri += ` type:"${show_types[i]}"`
        }

        uri += ')'
        
        uri += '&rows=100&sort=popularRank ASC'

        console.log(uri)

        let uri_encoded = encodeURI(uri);

        console.log(uri_encoded)

        let spell_check_uri = encodeURI(`/solr/shows/spell?q=title:${searchText}&amp;spellcheck=true&amp;spellcheck.count=10&amp;`)

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

        fetch(uri_encoded).then((data) => {
            data.json().then((resp) => {
                this.props.updateResults(resp['response']['docs'])
            })
        })
    }

    handleCheckbox = (position) => {
        const updatedCheckedState = this.state.checked.map((item, index) => index === position ? !item : item);
        this.state.checked = updatedCheckedState
    }

    render() {
        return (
            <Form className="search-form">
                <SearchBar ref={this.searchTextRef} />
                <Form.Group className="search-filters" controlId="searchFilters">
                    <Form.Group className="type-checkboxes" controlId="typeSearch">
                        <Form.Label>Type:</Form.Label>
                        {this.state.types.map((type, index) => (
                            <div key={type}>
                                <input
                                    type="checkbox"
                                    name="showtypes"
                                    value={`${type}`}
                                    defaultChecked={this.state.checked[index]}
                                    onChange={() => this.handleCheckbox(index)}
                                /> {`${type}`}
                            </div>
                        ))}
                    </Form.Group>

                    <Form.Group className="input-years" controlId="yearsSearch">
                        <div>
                            <Form.Label>Start Year:</Form.Label>
                            <div>
                                <input value={this.state.startYearInitial} onChange={evt => this.updateInputValue(evt,"startYearInitial")} type="number" min={0} max={3000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input value={this.state.startYearFinal} onChange={evt => this.updateInputValue(evt,"startYearFinal")} type="number" min={0} max={3000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>End Year:</Form.Label>
                            <div>
                                <input type="number" value={this.state.endYearInitial} onChange={evt => this.updateInputValue(evt,"endYearInitial")} min={0} max={3000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.endYearFinal} onChange={evt => this.updateInputValue(evt,"endYearFinal")} min={0} max={3000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>
                    </Form.Group>

                    <Form.Group className="input-episodes-runtime" controlId="episodesRuntimeSearch">
                        <div>
                            <Form.Label>Number of Episodes:</Form.Label>
                            <div>
                                <input type="number" value={this.state.numEpisodesInitial} onChange={evt => this.updateInputValue(evt,"numEpisodesInitial")} min={0} max={10000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.numEpisodesFinal} onChange={evt => this.updateInputValue(evt,"numEpisodesFinal")} min={0} max={10000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>Runtime:</Form.Label>
                            <div>
                                <input type="number" value={this.state.runtimeInitial} onChange={evt => this.updateInputValue(evt,"runtimeInitial")} min={0} max={10000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.runtimeFinal} onChange={evt => this.updateInputValue(evt,"runtimeFinal")} min={0} max={10000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>
                    </Form.Group>

                    <Form.Group className="input-rating-votes" controlId="ratingNumVotesSearch">
                        <div>
                            <Form.Label>Rating:</Form.Label>
                            <div>
                                <input type="number" value={this.state.ratingInitial} onChange={evt => this.updateInputValue(evt,"ratingInitial")} min={0} max={10} step={0.1} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.ratingFinal} onChange={evt => this.updateInputValue(evt,"ratingFinal")} min={0} max={10} step={0.1} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>Number of Votes:</Form.Label>
                            <div>
                                <input type="number" value={this.state.numVotesInitial} onChange={evt => this.updateInputValue(evt,"numVotesInitial")} min={0} max={1000000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" value={this.state.numVotesFinal} onChange={evt => this.updateInputValue(evt,"numVotesFinal")} min={0} max={1000000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
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
