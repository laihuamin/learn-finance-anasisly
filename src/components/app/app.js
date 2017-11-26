import React, {Component} from 'react';
import Btn from '../btn/btn.js';
import './app.less';
import ImgGroup from '../img-group/imgGroup.js';

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            nowLocal: 0,
            left: [],
            top: [],
            rorate: [],
            data: []
        }
    };
    formatData() {
        const left = [],
            top = [],
            rorate = [],
            data = [

            ];
        left = this.randomLeft();
        top = this.randomTop();
        rorate = this.randomRorate();
        this.setState({
            left,
            top,
            rorate,
            data
        })
    };
    randomLeft() {
        const left = [];
        for(let i = 0; i < this.state.data.length; i++){
            left[i] = Math.random()
        }
    };
    turn (n) {
        let _n = this.state.nowLocal + n;
        this.setState({nowLocal: _n});
    };
    componentDidMount(){
        this.formatData();
    }
    render () {
        return (
            <div className="app">
                <ImgGroup turn={this.turn.bind(this)} count={10} nowLocal={this.state.nowLocal} left={this.state.left} top={this.state.top} data={this.state.data} rorate={this.state.rorate}/>
                <Btn turn={this.turn.bind(this)} count={10} nowLocal={this.state.nowLocal}></Btn>
            </div>
        )
    };
}

export default App;