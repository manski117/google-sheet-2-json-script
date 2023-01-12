import React from 'react';
import { Component } from 'react';
import logo from '../logo.svg';




class Main extends Component{
    
    

    render(){
        let stuff = (
            <div className="main-container">
                {/* <img className='img0' src={logo} alt="A logo will go here" /> */}
                <div className="flexbox-main">
                    <h1 className='main-headline'>Fun facts about React</h1>
                    <ul className="list-main">
                            <li className="list-item">First released in 2013</li>
                            <li className="list-item">Originally created by Jordan Walke</li>
                            <li className="list-item">Well over 100k stars on github</li>
                            <li className="list-item">Maintained by facebook</li>
                            <li className="list-item">Powers thousands of enterprise apps, including mobile apps</li>
                    </ul>
                </div>
            </div>
            

        )
        return(
            stuff
        )
    }
}

export default Main;