import React from 'react'
import Result from './Result'

export default function SearchResults({ results, spellcheck }) {
    var words = [];
    for (let i in spellcheck) {
        words.push(spellcheck[i]['word'])
        if (i === "2") {
            break;
        }
    }
    console.log(words)
    return (
        results.length > 0 ?
            <div>
                <h3 className='num-results mt-4'>{results.length} results found</h3>
                {words.length > 0?
                    <div className='no-results'>
                        <tr >
                            <th className='collumn-h5'>
                                {spellcheck.length > 0 ? <p>Did you mean: </p> : ""}
                            </th>
                            {
                                words.map(word => {
                                    return (
                                        <th className='collumn' key={word}>
                                            {word}
                                        </th>
                                    )
                                })
                            }
                        </tr>
                    </div>
                :
                ""    
                }
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
            <div>
                <div className='no-results-message'>
                    <h3>No results found</h3>
                </div>
                <div className='no-results'>
                    <tr >
                        <th className='collumn-h5'>
                            {spellcheck.length > 0 ? <p>Did you mean: </p> : ""}
                        </th>
                        {
                            words.map(word => {
                                return (
                                    <th className='collumn' key={word}>
                                        {word}
                                    </th>
                                )
                            })
                        }
                    </tr>
                </div>
            </div>
    )
}
