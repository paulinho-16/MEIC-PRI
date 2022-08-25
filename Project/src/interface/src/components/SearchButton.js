import React, { Component } from 'react'
import Button from 'react-bootstrap/Button';

export class SearchButton extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <Button variant="danger" type="button" className="search-button" onClick={this.props.handleFunction}>
                Submit
            </Button>
        )
    }
}

export default SearchButton
