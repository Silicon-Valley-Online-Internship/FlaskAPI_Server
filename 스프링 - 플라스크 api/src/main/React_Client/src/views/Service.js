import React, { Fragment } from 'react';

import TopMenuComponent from 'component/TopMenuComponent';
import {Col, Container, Row} from "reactstrap";
import ServiceComponent from "component/ServiceComponent";

class Service extends React.Component {
    render() {
        return (
            <Fragment>
                <TopMenuComponent/>
                <main className="my-5 py-5">
                    <Container className="px-0">
                        <Row noGutters className="pt-2 pt-md-5 w-100 px-4 px-xl-0 position-relative">
                            <Col className="py-5 mb-5 py-md-0 mb-md-0">
                                <Fragment>
                                    <div className="position-relative">

                                    <span className="d-block pb-2 mb-0 h6 text-uppercase text-info font-weight-bold">
                                        Service Page
                                    </span>

                                        <span className="d-block pb-4 h2 text-dark border-bottom border-gray">FooDetector Service</span>

                                    </div>
                                    <ServiceComponent/>
                                </Fragment>
                            </Col>
                        </Row>
                    </Container>
                </main>
            </Fragment>
        )
    };
}

export default Service;