import React from 'react'
import '../css/TextInput.css'


export default class TextInput extends React.Component{
    constructor (props){
        super(props)
        this.state = {
            value : ""
        }
        this.changeUp = props.onChange;
        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(e){
        this.setState({
            value : e.target.value
        })
        this.changeUp(e.target.value)
    }


    render(){
        return(
        <div style={{paddingTop:'20px'}}> 
            <div>
                <textarea  className="from" value={this.state.value} onChange={this.handleChange}></textarea>
            </div>
            {/* <div className="split right">
                <input type="text"></input>
            </div> */}
        </div>
        )}
}