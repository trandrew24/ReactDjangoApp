import React, { Component } from 'react';
import RoomJoinPage from "./RoomJoinPage";
import createRoomPage from "./CreateRoomPage";
import { 
    BrowserRouter as Router,  // easier to write
    Switch, 
    Route, 
    Link, 
    Redirect,
} 
    from "react-router-dom"; // for the page routing system
import CreateRoomPage from './CreateRoomPage';

export default class HomePage extends Component {
    constructor(props) {
        // call parent constructor (Component constructor)
        super(props);
    }

    render() {
        return (
        // Router has Switch tags to select route for pages
        <Router>
            <Switch>

                {/* Designate the page '/' as the home page. exact keyword necessary to avoid the '/'
                character matching with other paths */}
                <Route exact path="/"> 
                    <p>This is the home page</p> 
                </Route>

                {/* Designate path /join as the component RoomJoinPage
                    RoomJoinPage is in curly braces because it is javascript code
                    embedded in HTML */}
                <Route path="/join" component={RoomJoinPage} />

                {/* Designate path /create as the component CreateRoomPage */}
                <Route path="/create" component={CreateRoomPage} />

            </Switch>
        </Router>);
    }
}