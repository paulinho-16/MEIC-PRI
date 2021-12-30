import 'bootstrap/dist/css/bootstrap.min.css'
import { Form, Button } from 'react-bootstrap'

function App() {
    return (
        <div className="form-container">
            <Form className="signup-form">
                <Form.Group>
                    <Form.Control className="name-input" type="text" placeholder="name" name="name"></Form.Control>
                    <Form.Control className="email-input" type="text" placeholder="email" name="email" ></Form.Control>
                    <Button className="submit-button" value="submit" type="submit">submit</Button>
                </Form.Group>
            </Form>
        </div>
    )
}

export default App;
