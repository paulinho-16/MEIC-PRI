import React, { Component } from 'react'
import ShowModal from './ShowModal'

import imageExists from "image-exists"

export default class Result extends Component {
    constructor(props) {
        super(props)

        this.state = {
            show: false,
            image: "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie-1-3.jpg" 
        }

        this.showModal = this.showModal.bind(this)
        this.hideModal = this.hideModal.bind(this)
        this.componentDidMount = this.componentDidMount.bind(this)
    }

    showModal() {
        this.setState({ show: true });
    }

    hideModal() {
        this.setState({ show: false })
    }

    componentDidMount() {
        const image = this.props.result['imageURL']
        
        if (this.props.result['imageURL'] === "https://m.media-amazon.com/images/G/01/imdb/images/social/imdb_logo.png")
        {
            this.props.result['imageURL'] = image
            return
        }

        imageExists(image, (im) => {
            if (im){
                this.setState({image})
            }
        })
    }

    render() {
        return (
            <>
                <div className='card text-center shadow'>
                    <div className='overflow'>
                        <img src={this.state.image} className='card-img-top' alt={`${this.props.result['title']} ${this.props.result['type']} poster`} />
                    </div>
                    <div className='card-body text-dark'>
                        <h4 className='card-title'>{this.props.result['title']}</h4>
                        <button className="btn btn-outline-danger" onClick={this.showModal}>More info</button>
                    </div>
                </div>

                <ShowModal result={this.props.result} show={this.state.show} image={this.state.image} hide={this.hideModal} />
            </>
        )
    }
}
