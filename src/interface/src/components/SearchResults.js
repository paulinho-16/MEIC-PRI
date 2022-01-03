import React from 'react'
import Result from './Result'

export default function SearchResults({ results }) {
    return (
        results.map(result => {
            return <Result key={result} result={result} />
        })
    )
}
