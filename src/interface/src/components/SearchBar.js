import React from 'react'
import Form from 'react-bootstrap/Form';
import { MDBInput } from 'mdb-react-ui-kit';

const SearchBar = React.forwardRef((props, ref) => {
    return (
        <Form.Group className="search-bar" controlId="formSearch">
            <MDBInput label='Search' id='searchInput' type='text' inputRef={ref} />
        </Form.Group>
    )
})

export default SearchBar