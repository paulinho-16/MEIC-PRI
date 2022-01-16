import React, { Component } from 'react'
import ShowModal from './ShowModal'

import urlExist from "url-exist"

export default class Result extends Component {
    constructor(props) {
        super(props)

        this.state = {
            show: false,
        }

        this.showModal = this.showModal.bind(this)
        this.hideModal = this.hideModal.bind(this)
        this.returnImage = this.returnImage.bind(this)
        this.checkIfImageExists = this.checkIfImageExists.bind(this)

        this.returnImage()
    }

    showModal() {
        this.setState({ show: true });
    }

    hideModal() {
        this.setState({ show: false })
    }

    async checkIfImageExists(url) {
        // const img = new Image();
        // img.src = url;

        // if (img.complete) {
        //     this.state.image = this.props.result['imageURL']
        //     return true
        // } else {
        //     img.onload = () => {
        //         this.state.image = this.props.result['imageURL']
        //         return true
        //     };

        //     img.onerror = () => {
        //         this.state.image = "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie-1-3.jpg"
        //         return false
        //     };
        // }

        // return true

        // const img = new Image();
        // img.src = url;

        let success
        try {
            success = await urlExist(url)
            console.log(success)
            this.props.result['imageURL'] = (success) ? this.props.result['imageURL'] : "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie-1-3.jpg"

            if (success) {
                console.log('cococ')
                console.log(this.props.result['imageURL'])
            }
            else{
                this.props.result['imageURL'] = "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie-1-3.jpg"

            }
        }
        catch {
            return false
        }
        // console.log(success)
        return success

        // const result = fetch(url, { method: 'HEAD' }).then(res => {
        //     if (res.ok) {
        //         //this.state.image = url
        //         console.log('Image exists.');
        //         return true
        //     } else {
        //         console.log('Image does not exist.');
        //         return false
        //     }
        // }).catch();
        // // console.log(result.ok)
        // return result.ok;
    }

    returnImage() {
        // this.checkIfImageExists(this.props.result['imageURL'], (exists) => {
        //     if (exists) {
        //         this.state.image = this.props.result['imageURL']
        //     } else {
        //         this.state.image = "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie-1-3.jpg"
        //     }

        //     // "https://m.media-amazon.com/images/G/01/imdb/images/social/imdb_logo.png"
        // });

        this.checkIfImageExists(this.props.result['imageURL'])


        //if (!exists)
        //console.log(exists)
        //console.log(exists)

        // if (exists) {
        //     this.state.image = this.props.result['imageURL']
        // } else {
        //     this.state.image = "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie-1-3.jpg"
        // }
    }

    render() {
        return (
            <>
                <div className='card text-center shadow'>
                    <div className='overflow'>
                        <img src={this.props.result['imageURL']} className='card-img-top' alt={`${this.props.result['title']} ${this.props.result['type']} poster`} />
                    </div>
                    <div className='card-body text-dark'>
                        <h4 className='card-title'>{this.props.result['title']}</h4>
                        <button className="btn btn-outline-danger" onClick={this.showModal}>More info</button>
                    </div>
                </div>

                <ShowModal result={this.props.result} show={this.state.show} hide={this.hideModal} />
            </>
        )
    }
}
