import React, {Component} from 'react';
import Btn from '../btn/btn.js';
import './app.less';

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            nowLocal: 0
        }
    };
    turn (n) {
        let _n = this.state.nowLocal + n;
        this.setState({nowLocal: _n});
    };
    render () {
        return (
            <div className="app">
                <Btn turn={this.turn.bind(this)} count={10} nowLocal={this.state.nowLocal}></Btn>
            </div>
        )
    };
}

export default App;