import React from 'react'
import Form from 'react-bootstrap/Form';

import SearchBar from './SearchBar';
import SearchButton from './SearchButton';

class SearchForm extends React.Component {
    constructor(props) {
        super(props)
        this.searchTextRef = React.createRef()
    }

    handleSearch = () => {
        const searchText = this.searchTextRef.current.value
        if (searchText === '') return
        console.log(searchText)
        let uri = `http://localhost:8983/solr/shows/select?indent=true&q.op=OR&q=title:${searchText} language:${searchText} summary:${searchText}`
        console.log(uri)
        let uri_encoded = encodeURI(uri);
        fetch(uri_encoded, {mode: 'cors'}).then((data) => {
            data.json().then((resp) => {
                console.warn("resp", resp)
            })
        })

        // TODO: ver qual a melhor forma de fazer queries ao Solr
        // fetch é bloqueado por falta de CORS
    }

    render() {
        return (
            <Form className="search-form">
                <SearchBar ref={this.searchTextRef}/>
                <SearchButton handleFunction={this.handleSearch}/>
            </Form>
        )
    }
}

export default SearchForm
