import React, { Component } from 'react'
import ShowModal from './ShowModal'

export default class Result extends Component {
    constructor(props) {
        super(props)

        this.state = {
            show: false
        }

        this.showModal = this.showModal.bind(this)
        this.hideModal = this.hideModal.bind(this)
    }

    showModal() {
        this.setState({ show: true });
    }

    hideModal() {
        this.setState({ show: false })
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
