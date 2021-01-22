import React, {Component, Fragment} from "react";
import {Col, Container, Row} from "reactstrap";


class HomeComponent extends Component {
    render() {
        return (
            <main className="my-5 py-5">
                <Container className="px-0">
                    <Row noGutters className="pt-2 pt-md-5 w-100 px-4 px-xl-0 position-relative">
                        <Col className="py-5 mb-5 py-md-0 mb-md-0">
                            <Fragment>
                                <div className="position-relative">
                                    <span className="d-block pb-2 mb-0 h6 text-uppercase text-info font-weight-bold">
                                        Home
                                    </span>

                                    <span className="d-block pb-4 h2 text-dark border-bottom border-gray">FooDetector Project</span>

                                    <article className="pt-5 text-secondary text-justify" style={{ fontSize: '0.9rem', whiteSpace: 'pre-line' }}>
                                        팀 CoCo(Corona Coder)의 FooDetector 를 소개합니다.<br/>
                                        Introducing CoCo(Corona Coder) Team's FooDetector<br/>
                                        <br/>
                                        이 프로젝트는 사진 내의 음식을 인식하고 학습된 데이터를 기반하여 편리한 기능을 지원하는 웹기반 프로젝트입니다.<br/>
                                        This project is a web-based project that supports a function that recognizes food in pictures.<br/>
                                    </article>
                                </div>
                            </Fragment>
                        </Col>
                    </Row>
                </Container>
            </main>
        )
    }
}

export default HomeComponent