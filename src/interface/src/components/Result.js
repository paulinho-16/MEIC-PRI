import React from 'react'

export default function Result({ result }) {
    return (
        <div className='card text-center shadow'>
            <div className='overflow'>
                <img src={result['imageURL']} className='card-img-top' alt={`${result['title']} ${result['type']} poster`} />
            </div>
            <div className='card-body text-dark'>
                <h4 className='card-title'>{result['title']}</h4>
                <p className='card-text text-secondary'>
                    {result['summary']}
                </p>
                <a href='#' className='btn btn-outline-success'>More info</a>
            </div>
        </div>
    )
}
