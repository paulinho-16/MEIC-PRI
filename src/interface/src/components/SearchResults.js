import React from 'react'
import Result from './Result'

export default function SearchResults({ results }) {
    return (
        results.length > 0 ?
            <div>
                <h3 className='num-results mt-4'>{results.length} results found</h3>
                <div className='container-fluid d-flex justify-content-center'>
                    <div className='row pt-5'>
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
            </div>
            :
            <div className='no-results'>
                <h3>No results found</h3>
            </div>
    )
}
