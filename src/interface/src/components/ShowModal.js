import React, { Component } from 'react'
import Modal from "react-bootstrap/Modal";
import Button from 'react-bootstrap/Button';
import ListGroup from 'react-bootstrap/ListGroup';

export default class ShowModal extends Component {
    constructor(props) {
        super(props)
        this.genres = this.props.result['genres'].replace(/[^a-zA-Z ]/g, "").split(" ")
    }

    render() {
        return (
            <Modal show={this.props.show} onHide={this.props.hide} className='showModal'>
                <Modal.Dialog className='showModal-content'>
                    <Modal.Header closeButton className='showModal-header'>
                        <Modal.Title>{this.props.result['title']}</Modal.Title>
                    </Modal.Header>

                    <Modal.Body className='showModal-body'>
                        <div className='popup-image'>
                            <img src={this.props.result['imageURL']} className='card-img-popup' alt={`${this.props.result['title']} ${this.props.result['type']} poster`} />
                            <div className='imdb-rating-box'>
                                Rating: <span className='imdb-rating-text'> {this.props.result['rating']}</span>
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/2560px-IMDB_Logo_2016.svg.png" className='imdb-rating' alt="IMDb Rating" />
                            </div>
                        </div>
                        <div className="popup-info">
                            <div>
                                <Button variant="danger" className='popular-rank' >
                                    <span variant="danger"> {this.props.result['popularRank']}</span>
                                </Button>

                            </div>
                            <ListGroup horizontal>
                                {
                                    this.genres.map(genre => {
                                        return (
                                            <ListGroup.Item key={genre} variant="danger">{genre}</ListGroup.Item>
                                        )
                                    })
                                }
                            </ListGroup >
                            <h3 className="popup-title">Description</h3>
                            <div className="popup-summary">
                                {this.props.result['summary']}
                            </div>
                            <table>
                                <tbody>
                                    <tr>
                                        <th>Language:</th>
                                        <td>{this.props.result['language']}</td>
                                    </tr>
                                    <tr>
                                        <th>Origin Country:</th>
                                        <td>{this.props.result['originCountry']}</td>
                                    </tr>
                                    <tr>
                                        <th>Runtime:</th>
                                        <td>{this.props.result['runtime']}</td>
                                    </tr>
                                    <tr>
                                        <th>Year of Release:</th>
                                        <td>{this.props.result['startYear']}</td>
                                    </tr>
                                    {this.props.result['endYear']}
                                    <tr>
                                        <th>Type:</th>
                                        <td>{this.props.result['type']}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <p>{this.props.result['summary']}</p>
                    </Modal.Body>

                    <Modal.Footer className='showModal-footer'>
                        <p>Footer</p>
                    </Modal.Footer>
                </Modal.Dialog>
            </Modal>
        )
    }
}
