import logo from "./logo.svg";
import "./App.css";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import NumericInput from "react-numeric-input";
import DropdownMultiselect from "react-multiselect-dropdown-bootstrap";
import Multiselect from "multiselect-react-dropdown";
import Nav from "react-bootstrap/Nav";
import Form from "react-bootstrap/Form";
import { Row, Col } from "react-bootstrap";
// require('./dropdown.js');
import SearchForm from "./components/SearchForm";
import SearchResults from "./components/SearchResults";
import React from "react";

// var state = {
//     options: [{ name: 'animation', id: 1 }, { name: 'miniSeries', id: 2 }, { name: 'movie', id: 3 }, { name: 'series', id: 4 }, { name: 'short', id: 5 }, { name: 'special', id: 6 }]
// };

class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			results: [],
			spellcheck: [],
		};
	}

	updateResults = (results) => {
		this.setState({ results: results });
	};

	updateSpellCheck = (spellcheck) => {
		this.setState({ spellcheck: spellcheck });
	};

	render() {
		return (
			<div
				className="App"
				style={{
					background:
						this.state.results.length > 0 ? "radial-gradient(#e5e5e5, #ffff, #e5e5e5)" : "none",
				}}
			>
				<header className="App-header">
					<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Netflix_2015_logo.svg/2560px-Netflix_2015_logo.svg.png" className="netflix-logo" alt="Netflix logo" />
				</header>
				<div className='content'>
					<SearchForm updateResults={this.updateResults} updateSpellCheck={this.updateSpellCheck} />
					<SearchResults results={this.state.results} spellcheck={this.state.spellcheck} />
				</div>
			</div>
		);
	}
}

export default App;
