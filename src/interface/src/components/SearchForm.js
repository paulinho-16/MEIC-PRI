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
            endYearFinal: null || ''
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

        
        console.log(this.state.startYearInitial)
    }

    handleSearch = () => {
        const searchText = this.searchTextRef.current.value        
        const show_types = this.state.types.filter((_, index) => this.state.checked[index]);
        console.log(show_types)

        let uri = null
        if (searchText === '') // TODO: recolher apenas alguns de todos os resultados (paginação?)
            uri = `/solr/shows/select?indent=true&q.op=OR&q=*:*`
        else
            uri = `/solr/shows/select?indent=true&q.op=OR&q=title:"${searchText}"` // TODO: language:"${searchText}" summary:"${searchText}" 

        if (this.state.startYearInitial > 0 & this.state.startYearFinal >0 )
        {
            uri = uri + ` startYear:[${this.state.startYearInitial} TO ${this.state.startYearFinal}]`
            uri = uri.replace("q.op=OR","q.op=AND")
        }
        else if (this.state.startYearInitial > 0)
        {
            uri = uri + ` startYear:[${this.state.startYearInitial} TO 9999]`
            uri = uri.replace("q.op=OR","q.op=AND")
        }
        else if (this.state.startYearFinal > 0 )
        {
            uri = uri + ` startYear:[1 TO ${this.state.startYearFinal}]`
            uri = uri.replace("q.op=OR","q.op=AND")
        }
        else {
            this.state.startYearInitial = ""
            this.state.startYearFinal = ""
        }

        if (this.state.endYearInitial > 0 & this.state.endYearFinal >0 )
        {
            uri = uri + ` endYear:[${this.state.endYearInitial} TO ${this.state.endYearFinal}]`
            uri = uri.replace("q.op=OR","q.op=AND")
        }
        else if (this.state.endYearInitial > 0)
        {
            uri = uri + ` endYear:[${this.state.endYearInitial} TO 9999]`
            uri = uri.replace("q.op=OR","q.op=AND")
        }
        else if (this.state.endYearFinal > 0 )
        {
            uri = uri + ` endYear:[1 TO ${this.state.endYearFinal}]`
            uri = uri.replace("q.op=OR","q.op=AND")
        }
        else {
            this.state.endYearInitial = ""
            this.state.endYearFinal = ""
        }

        uri = uri + "&rows=20"
        
        console.log(uri)

        let uri_encoded = encodeURI(uri);

        console.log(uri_encoded)

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
                                <Form.Check
                                    type='checkbox'
                                    id={`${type}`}
                                    label={`${type}`}
                                    defaultChecked={this.state.checked[index]}
                                    onChange={() => this.handleCheckbox(index)}
                                />
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
                                <input type="number" min={0} max={10000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" min={0} max={10000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>Runtime:</Form.Label>
                            <div>
                                <input type="number" min={0} max={10000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" min={0} max={10000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>
                    </Form.Group>

                    <Form.Group className="input-rating-votes" controlId="ratingNumVotesSearch">
                        <div>
                            <Form.Label>Rating:</Form.Label>
                            <div>
                                <input type="number" min={0} max={10000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" min={0} max={10000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                            </div>
                        </div>

                        <div>
                            <Form.Label>Number of Votes:</Form.Label>
                            <div>
                                <input type="number" min={0} max={10000} style={{marginRight:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
                                TO
                                <input type="number" min={0} max={10000} style={{marginLeft:'1rem'}} onKeyDown={(evt) => evt.key === 'e' && evt.preventDefault()} />
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
