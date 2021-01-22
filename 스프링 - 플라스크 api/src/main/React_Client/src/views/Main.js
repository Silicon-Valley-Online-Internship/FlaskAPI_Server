import React, { Fragment } from 'react';

import TopMenuComponent from 'component/TopMenuComponent';
import {Col, Container, Row} from "reactstrap";
import MainComponent from "component/MainComponent";

class Main extends React.Component {
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
                                        Main Page
                                    </span>

                                        <span className="d-block pb-4 h2 text-dark border-bottom border-gray">FooDetector Project</span>

                                        {/*<article className="pt-5 text-secondary text-justify" style={{ fontSize: '0.9rem', whiteSpace: 'pre-line' }}>*/}
                                        {/*    Main 페이지 입니다 <br/>*/}
                                        {/*</article>*/}

                                    </div>
                                    <MainComponent/>
                                </Fragment>
                            </Col>
                        </Row>
                    </Container>
                </main>
            </Fragment>
        )
    };
}

export default Main;