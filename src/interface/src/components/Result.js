import React, { Component } from 'react';
import CloseButton from 'react-bootstrap/CloseButton'
import ListGroup from 'react-bootstrap/ListGroup'
import Button from 'react-bootstrap/Button'

export class Result extends Component {
    constructor(props) {
        super(props)
        this.state = {
            result: props.result
        };
    }

    handleClick = () => {
        var modal = document.getElementById("CardModal" + this.state.result['imdbID']);
        modal.style.display = "block";
    }

    handleClickClose = () => {
        var modal = document.getElementById("CardModal" + this.state.result['imdbID']);
        modal.style.display = "none";
    }

    render() {
        var endYear;
        if (this.state.result["endYear"] & this.state.result["type"] === "series") {
            endYear = <tr><th>End Year:</th><td>{this.state.result["endYear"]}</td></tr>;
        }
        else if (this.state.result["type"] === "series") {
            endYear = <tr><th>End Year:</th><td>-</td></tr>;
        }
        else {
            endYear = ""
        }

        var genres = [];

        genres = this.state.result["genres"]
        genres = genres.replace(/[^a-zA-Z ]/g, "")
        genres = genres.split(" ")

        return (
            <div className='card text-center shadow'>
                <div className='imdb-rating-main'>
                    <span className='imdb-rating-text'> {this.state.result['rating']}</span>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/2560px-IMDB_Logo_2016.svg.png" className='imdb-rating' alt="imdb rating" />
                </div>
                <div className='overflow'>
                    <img src={this.state.result['imageURL']} className='card-img-top' alt={`${this.state.result['title']} ${this.state.result['type']} poster`} />
                </div>
                <div className='card-body text-dark'>
                    <h4 className='card-title'>{this.state.result['title']}</h4>
                    <p className='card-text text-secondary'>
                        {this.state.result['summary']}
                    </p>

                    <button id="CardButton" className='btn btn-outline-success' onClick={this.handleClick}>More Info</button>

                    <div id={`CardModal${this.state.result['imdbID']}`} className="modal">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h2>{this.state.result['title']}</h2>
                                <CloseButton onClick={this.handleClickClose} />
                            </div>
                            <div className="modal-body">
                                <div className='popup-image'>
                                    <img src={this.state.result['imageURL']} className='card-img-popup' alt={`${this.state.result['title']} ${this.state.result['type']} poster`} />
                                    <div className='imdb-rating-box'>
                                        Rating: <span className='imdb-rating-text'> {this.state.result['rating']}</span>
                                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/2560px-IMDB_Logo_2016.svg.png" className='imdb-rating' alt="imdb rating" />
                                    </div>
                                </div>
                                <div className="popup-info">
                                    <div>
                                        <Button variant="danger" className='popular-rank' >
                                            <span variant="danger"> {this.state.result['popularRank']}</span>
                                        </Button>

                                    </div>
                                    <ListGroup horizontal>
                                        {
                                            genres.map(genre => {
                                                return (
                                                    <ListGroup.Item variant="danger">{genre}</ListGroup.Item>
                                                )
                                            })
                                        }
                                    </ListGroup >
                                    <h3 className="popup-title">Description</h3>
                                    <div className="popup-summary">
                                        {this.state.result['summary']}
                                    </div>
                                    <table>
                                        <tbody>
                                            <tr>
                                                <th>Language:</th>
                                                <td>{this.state.result['language']}</td>
                                            </tr>
                                            <tr>
                                                <th>Origin Country:</th>
                                                <td>{this.state.result['originCountry']}</td>
                                            </tr>
                                            <tr>
                                                <th>Runtime:</th>
                                                <td>{this.state.result['runtime']}</td>
                                            </tr>
                                            <tr>
                                                <th>Year of Release:</th>
                                                <td>{this.state.result['startYear']}</td>
                                            </tr>
                                            {endYear}
                                            <tr>
                                                <th>Type:</th>
                                                <td>{this.state.result['type']}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div className="modal-footer">
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        )
    }
}

export default Result
