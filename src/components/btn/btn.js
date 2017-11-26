import React, {Component} from 'react';
import './btn.less';

class Btn extends React.Component {
    constructor(props) {
        super(props);
    }
    handleClickBtn(i) {
        let option = i - this.props.nowLocal;
        this.props.turn(option);
    }
    render() {
        let btnNodes = [];
        let {count, nowLocal} = this.props;
        for(let i = 0; i < count; i++) {
            btnNodes[i] = (<span
                key = {`dot${i}`}
                className = { "btn" + (i === nowLocal ? " active" : "")}
                onClick={this.handleClickBtn.bind(this, i)}
            ></span>)
        }
        return (
            <div className="btn-group">{btnNodes}</div>
        )
    }
}

export default Btn;