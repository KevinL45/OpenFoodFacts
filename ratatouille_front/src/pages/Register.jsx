import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function Register() {
  return (
    <Form>
    <Form.Group className="mb-3" controlId="formBasicFirstname">
        <Form.Label>Prénom</Form.Label>
        <Form.Control type="text" placeholder="Enter firstname" />
    </Form.Group>
    <Form.Group className="mb-3" controlId="formBasicLastname">
        <Form.Label>Nom</Form.Label>
        <Form.Control type="text" placeholder="Enter Lastname" />
    </Form.Group>
    <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>E-mail</Form.Label>
        <Form.Control type="email" placeholder="Enter email" />
    </Form.Group>
    <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Mot de passe</Form.Label>
        <Form.Control type="password" placeholder="Password" />
    </Form.Group>
    <Button variant="primary" type="submit">
        S'inscrire
    </Button>
    </Form>
  );
}
export default Register;