import React from 'react'
import Result from './Result'

export default function SearchResults({ results }) {
    return (
        results.length > 0 ?
            <div>
                {
                    results.map(result => {
                        return <Result key={result['imdbID']} result={result} />
                    })
                }
            </div>
            :
            <div className='no-results'>
                <h3>No results found</h3>
            </div>
    )
}
