import React from 'react';
import { Component } from 'react';
import logo from '../logo.svg';




class Navbar extends Component{
    
    

    render(){
        let stuff = (
            <nav className="navbar">
                <div className="flexbox1">
                    <img className='img-nav-logo' src={logo} alt="" srcset="" />
                    <h2 className='nav-headline'>ReactFacts</h2>
                </div>
                <h4 className='nav-subhead'>Learn React - Course 1</h4>
            </nav>
            

        )
        return(
            stuff
        )
    }
}

export default Navbar;