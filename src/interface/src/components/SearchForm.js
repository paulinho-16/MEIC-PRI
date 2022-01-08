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
        let uri = null
        if (searchText === '') // TODO: recolher apenas alguns de todos os resultados (paginação?)
            uri = `/solr/shows/select?indent=true&q.op=OR&q=*:*&rows=20`
        else
            uri = `/solr/shows/select?indent=true&q.op=OR&q=title:"${searchText}" language:"${searchText}" summary:"${searchText}"&rows=6216`
        let uri_encoded = encodeURI(uri);

        fetch(uri_encoded).then((data) => {
            data.json().then((resp) => {
                this.props.updateResults(resp['response']['docs'])
            })
        })
    }

    render() {
        return (
            <Form className="search-form">
                <SearchBar ref={this.searchTextRef} />
                <SearchButton handleFunction={this.handleSearch} />
            </Form>
        )
    }
}

export default SearchForm
