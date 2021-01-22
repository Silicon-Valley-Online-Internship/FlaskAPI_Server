import React, {Component} from "react";
//import {Navbar} from "react-bootstrap";
import {
    Container, Row, Col, Navbar, Nav, NavLink, NavItem
} from 'reactstrap';
// import {BrowserRouter as Router, Route} from "react-router-dom";
//
// import MainComponent from './MainComponent'
// import ServiceComponent from './ServiceComponent'
// import HomeComponent from "./HomeComponent";

class TopMenuComponent extends Component {
    render() {
        return (
            // <Router>
            //     <Navbar
            //         bg="dark"
            //         variant="dark"
            //         className="mb-4">
            //         <Navbar.Brand href="/home">
            //             Home
            //         </Navbar.Brand>
            //         <Navbar.Brand href="/main">
            //             Main
            //         </Navbar.Brand>
            //         <Navbar.Brand href="/service">
            //             Service
            //         </Navbar.Brand>
            //     </Navbar>
            //
            //     <Route path="/home" component={HomeComponent}/>
            //     <Route path="/main" component={MainComponent}/>
            //     <Route path="/service" component={ServiceComponent}/>
            // </Router>

            /*새로 바꾼 부분*/
            <header>
                <Navbar fixed="top" color="light" light expand="xs" className="border-bottom border-gray bg-white" style={{ height: 80 }}>

                    <Container>
                        <Row noGutters className="position-relative w-100 align-items-center">

                            <Col className="d-none d-lg-flex justify-content-start">
                                <Nav className="mrx-auto" navbar>

                                    <NavItem className="d-flex align-items-center">
                                        <NavLink className="font-weight-bold" href="/home">Home</NavLink>
                                    </NavItem>

                                    <NavItem className="d-flex align-items-center">
                                        <NavLink className="font-weight-bold" href="/main">Main</NavLink>
                                    </NavItem>

                                    <NavItem className="d-flex align-items-center">
                                        <NavLink className="font-weight-bold" href="/service">Service</NavLink>
                                    </NavItem>
                                </Nav>
                            </Col>
                        </Row>
                    </Container>
                </Navbar>
            </header>
        )
    }
}

export default TopMenuComponent;