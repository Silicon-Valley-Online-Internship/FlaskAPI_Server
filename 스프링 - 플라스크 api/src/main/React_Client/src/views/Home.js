import React, { Fragment } from 'react';

import TopMenuComponent from "component/TopMenuComponent";
import HomeComponent from "../component/HomeComponent";

class Home extends React.Component {
    render() {
        return (
            <Fragment>
                <TopMenuComponent />
                <HomeComponent />
            </Fragment>
        )
    };
}

export default Home;