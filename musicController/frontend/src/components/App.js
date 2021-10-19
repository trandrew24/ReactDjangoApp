import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage"; // put HomePage component in App component

/* IMPORTANT: I'm using class components here, but it is generally best
practice to use functional components. Consider a refactor later to
use functional components instead (and learn how to use functional) */


/* Render this component inside of the div found in the html. Put the component inside of app container.
 App is first component to be rendered. App will render other components */
export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        
        // render HomePage component in App component
        return  (
            // Return the div that contains the components we made
            <div>
            <HomePage />
            </div>
        );
    }
}

const appDiv = document.getElementById("app");

// render and shove the App component inside appDiv that is in templates/frontend/index.html
render(<App/>, appDiv);