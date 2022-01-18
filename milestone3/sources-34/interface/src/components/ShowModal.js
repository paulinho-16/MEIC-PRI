import React, { Component } from 'react'
import Modal from "react-bootstrap/Modal";
import Button from 'react-bootstrap/Button';
import ListGroup from 'react-bootstrap/ListGroup';
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'

export default class ShowModal extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        var endYear;
        if (this.props.result["endYear"] && this.props.result["type"] === "series") {
            endYear = <tr><th>End Year:</th><td>{this.props.result["endYear"]}</td></tr>;
        }
        else if (this.props.result["type"] === "series") {
            endYear = <tr><th>End Year:</th><td>-</td></tr>;
        }
        else {
            endYear = ""
        }

        var startYear;
        if (this.props.result["startYear"] && (this.props.result["type"] === "series" || this.props.result["type"] === "miniSeries")) {
            startYear = <tr><th>Year of Release:</th><td>{this.props.result["startYear"]}</td></tr>;
        }
        else if (this.props.result["type"] === "series" || this.props.result["type"] === "miniSeries") {
            startYear = <tr><th>Year of Release:</th><td>-</td></tr>;
        }
        else {
            startYear = ""
        }

        var episodes;
        if (this.props.result["episodes"] && (this.props.result["type"] === "series" || this.props.result["type"] === "miniSeries" || this.props.result["type"] === "movie")) {
            episodes = <tr><th>Episodes:</th><td>{this.props.result["episodes"]}</td></tr>;
        }
        else if (this.props.result["type"] === "series" || this.props.result["type"] === "miniSeries") {
            episodes = <tr><th>Episodes:</th><td>-</td></tr>;
        }
        else {
            episodes = "";
        }

        var cast;
        if (this.props.result["cast"]) {
            let c = String(this.props.result['cast']).replace(/[^a-zA-Z, ]/g, "");
            cast = <div>{c}</div>;
        }
        else {
            cast = <div>Not Available</div>;
        }

        var language;
        if (this.props.result['language']) {
            language = <tr><th>Language:</th><td>{this.props.result['language']}</td></tr>
        }
        else {
            language = ""
        }

        var originCountry;
        if (this.props.result['originCountry']) {
            originCountry = <tr><th>Origin Country:</th><td>{this.props.result['originCountry']}</td></tr>
        }
        else {
            originCountry = ""
        }

        var runtime;
        if (this.props.result['runtime']) {
            runtime = <tr><th>Runtime:</th><td>{this.props.result['runtime']}</td></tr>
        }
        else {
            runtime = ""
        }

        this.genres = String(this.props.result['genres']).replace(/[^a-zA-Z ]/g, "").split(" ")

        var certificates;
        if (this.props.result['certificate']) {
            let cert = String(this.props.result['certificate']).replace(/[^a-zA-Z,:\d+ -]/g, "")
            certificates = <div>{cert}</div>;
        }
        else {
            certificates = <div>Not Available</div>;
        }

        var numVotes;
        if (this.props.result['numVotes']) {
            numVotes = <tr><th>Number of Votes:</th><td>{this.props.result['numVotes']}</td></tr>
        }
        else {
            numVotes = ""
        }

        var type;
        type = <tr><th>Type:</th><td>{this.props.result['type']}</td></tr>

        return (
            <Modal show={this.props.show} onHide={this.props.hide} className='showModal'>
                <Modal.Header closeButton className='showModal-header'>
                    <Modal.Title>{this.props.result['title']}</Modal.Title>
                </Modal.Header>

                <Tabs defaultActiveKey="info" id="uncontrolled-tab-example" className="mb-3">
                    <Tab eventKey="info" title="Info">
                        <Modal.Body className='showModal-body'>
                            <div className='popup-image'>
                                <img src={this.props.image} className='card-img-popup' alt={`${this.props.result['title']} ${this.props.result['type']} poster`} />
                                <div className='imdb-rating-box'>Rating:<span className='imdb-rating-text'>{this.props.result['rating']}</span>
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/2560px-IMDB_Logo_2016.svg.png" className='imdb-rating' alt="IMDb Rating" />
                                </div>
                            </div>
                            <div className="popup-info">
                                <div>
                                    <Button title="Polpular Rank" variant="danger" className='popular-rank' >
                                        <span variant="danger">{this.props.result['popularRank']}</span>
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
                                        {type}
                                        {language}
                                        {originCountry}
                                        {runtime}
                                        {startYear}
                                        {endYear}
                                        {episodes}
                                        {numVotes}
                                    </tbody>
                                </table>
                            </div>
                        </Modal.Body>
                    </Tab>
                    <Tab eventKey="cast" title="Cast">
                        <Modal.Body className='showModal-body'>
                            <div className='popup-image'>
                                <img src={this.props.image} className='card-img-popup' alt={`${this.props.result['title']} ${this.props.result['type']} poster`} />
                                <div className='imdb-rating-box'>Rating:<span className='imdb-rating-text'>{this.props.result['rating']}</span>
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/2560px-IMDB_Logo_2016.svg.png" className='imdb-rating' alt="IMDb Rating" />
                                </div>
                            </div>
                            <div className="popup-info">
                                <div>
                                    <Button title="Polpular Rank" variant="danger" className='popular-rank' >
                                        <span variant="danger">{this.props.result['popularRank']}</span>
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
                                <h3 className="popup-title">Cast</h3>
                                <div className="popup-summary">
                                    {cast}
                                </div>
                            </div>
                        </Modal.Body>
                    </Tab>
                    <Tab eventKey="certificates" title="Certificates">
                        <Modal.Body className='showModal-body'>
                            <div className='popup-image'>
                                <img src={this.props.image} className='card-img-popup' alt={`${this.props.result['title']} ${this.props.result['type']} poster`} />
                                <div className='imdb-rating-box'>Rating:<span className='imdb-rating-text'>{this.props.result['rating']}</span>
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/2560px-IMDB_Logo_2016.svg.png" className='imdb-rating' alt="IMDb Rating" />
                                </div>
                            </div>
                            <div className="popup-info">
                                <div>
                                    <Button title="Polpular Rank" variant="danger" className='popular-rank' >
                                        <span variant="danger">{this.props.result['popularRank']}</span>
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
                                <h3 className="popup-title">Certificates</h3>
                                <div className="popup-summary">
                                    {certificates}
                                </div>
                            </div>
                        </Modal.Body>
                    </Tab>
                </Tabs>
                <Modal.Footer className='showModal-footer'>
                    <p> </p> 
                    {/* &zwnj; */}
                </Modal.Footer>
            </Modal>
        )
    }
}
