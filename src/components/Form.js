import React from 'react'
import ReactDOM from 'react-dom'
import TextInput from './TextInput.js'

const path = require('path')


export default class MainForm extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            from : "",
            to : "",
            choice : "",
            choiceL : ""
        }
        this.handleChanges = this.handleChanges.bind(this)
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }    

    handleChanges(text){    
        this.setState({from : text})
    }

    handleChange(event){
        this.setState({[event.target.name] : event.target.value})
    }

    handleSubmit(){
        // console.log(this.state)
        // console.log(this.state.files)
        this.setState({to : ""})
        // var files = Array.from(this.state.files).map(file => file.name);
        // console.log(this.state.choice)
        // if(this.state.choice != "" && this.state.files && this.state.key){
        
        // this.setState({warning : ""})
        // console.log(this.state.choiceL)
        fetch("http://localhost:5000/".concat(this.state.choice).concat(this.state.choiceL),{
        method : 'post',
        headers : {'Content-type' : 'application/json'},
        body : JSON.stringify({
            sentence : this.state.from
            })
        }).then(res => res.json())
            .then(data => this.setState({to : data.data}))
            .then (e => console.log(this.state.to))
                .catch(err => console.log(err))
        // }else{
            // this.setState({warning : "ISI YANG BENER"})
        // }
            // console.log(this.state.hasils)
        // console.log(this.state.to)
    }

    render(){
        return (
            <div>
                <div>
                    <div>
                        {/* <input name="files" type="file" onChange={this.handleChange} required multiple /> */}
                        {/* <input type="text" name="dir"/> */}
                    </div>
                    <div>
                        <div><input name="choice" type="radio" value="kmp" onChange={this.handleChange}/>KMP</div>
                        <div><input name="choice" type="radio" value="regex" onChange={this.handleChange}/>REGEX</div>
                        <div><input name="choice" type="radio" value="bm" onChange={this.handleChange}/>BOYERMOORE</div>
                    </div>
                    <div>
                        <div><input name="choiceL" type="radio" value="si" onChange={this.handleChange}/>Sunda - Indonesia</div>
                        <div><input name="choiceL" type="radio" value="is" onChange={this.handleChange}/>Indonesia - Sunda</div>
                    </div>
                    <div>
                        <TextInput onChange={this.handleChanges}/>
                    </div>
                    <div>
                        {/* <h1>{this.state.warning ? this.state.warning : ""}</h1> */}
                        <button onClick={this.handleSubmit} name="submit">Translate</button>
                    </div>
                    <div>
                        {this.state.to ? "Translated : " +this.state.to : ""}
                    </div>
                </div>
            </div>
        )
    }
}