import React, {Component} from 'react';
import './imgGroup.less';

class ImgGroup extends React.Component{
    constructor(props) {
        super(props);
    }
    handleImg(n) {
        this.props.turn(n);
    }
    render() {
        let imgNodes = [];
        let {count, data, nowLocal, left, top, rorate} = this.props;
        for(let i = 0; i < count; i++) {
            imgNodes[i] = (<div 
                key={`img${i}`}
                onClick={this.handleImg.bind(this, i)}
                className={"img-item" + (i === nowLocal ? " " : "")}
                style={{
                    left: `${left[i]}%`,
                    top: `${top[i]}%`,
                    transform: `rotate(${rorate[i]}deg)`
                }}>
                <img src={data[i].img} className="image"/>
                <h2 className="img-desc">{data[i].title}</h2>
            </div>)
        }
        return (
            <div className="img-wrapper">{imgNodes}</div>
        )
    }
}

export default ImgGroup;