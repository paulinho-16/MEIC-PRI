import React from 'react'
import Result from './Result'

export default function SearchResults({ results }) {
    return (
        results.length > 0 ?
            <div className='container-fluid d-flex justify-content-center'>
                <div className='row'>
                    {
                        results.map(result => {
                            return (
                                <div className='col' key={result['imdbID']}>
                                    <Result result={result} />
                                </div>
                            )
                        })
                    }
                </div>
            </div>
            :
            <div className='no-results'>
                <h3>No results found</h3>
            </div>
    )
}
