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
        const left = this.randomLeft(),
            top = this.randomTop(),
            rorate = this.randomRorate(),
            data = [];
        for(let i = 0; i < 10; i++) {
            data[i] = Object.assign({}, {
                img: 'http://img.htmleaf.com/1507/3d-club-images-2.jpg',
                title: '小勺子'
            });
        }
        this.setState({
            left: left,
            top: top,
            rorate: rorate,
            data: data
        })
    };
    randomLeft() {
        const left = [];
        for(let i = 0; i < 5; i++){
            left[i] = Math.floor(Math.random() * 20);
        }
        for(let i = 5; i < 10; i++){
            left[i] = Math.floor(Math.random() * 20 + 80);
        }
        return left;
    };
    randomTop() {
        const top = [];
        for(let i = 0; i < 10; i++){
            top[i] = Math.floor(Math.random() * 80);
        }
        return top;
    };
    randomRorate() {
        const rorate = [];
        for(let i = 0; i < 5; i++){
            rorate[i] = Math.floor(Math.random() * 45);
        }
        for(let i = 5; i < 10; i++){
            rorate[i] = -Math.floor(Math.random() * 45);
        }
        return rorate;
    }
    turn (n) {
        let _n = this.state.nowLocal + n;
        this.setState({nowLocal: _n});
    };
    componentWillMount(){
        this.formatData();
    }
    render () {
        console.log(this.state);        
        return (
            <div className="app">
                <ImgGroup turn={this.turn.bind(this)} count={10} nowLocal={this.state.nowLocal} left={this.state.left} top={this.state.top} data={this.state.data} rorate={this.state.rorate}/>
                <Btn turn={this.turn.bind(this)} count={10} nowLocal={this.state.nowLocal}></Btn>
            </div>
        )
    };
}

export default App;