import React, {Component} from 'react';
import Btn from '../btn/btn.js';

class App extends React.Component{
    constructor(props) {
        super(props);
    };
    turn () {
    };
    render () {
        return (
            <div className="app">
                <Btn turn={this.turn} count={10} nowLocal={1}></Btn>
            </div>
        )
    };
}

export default App;