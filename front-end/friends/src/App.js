import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import { Link } from "react-router-dom";

function App() {
  const [friends, setFriends] = useState([]);
  useEffect(() => {
    const data = axios.get("http://localhost:8000").then((res) => {
      setFriends(res.data);
    });
  }, []);

  const refactor = (url) => {
    if (url !== null) {
      let new_url = url.replace(/^(?:https?:\/\/)?(?:www\.)?/i, "");
      new_url = new_url.split("=")[1];
      return new_url;
    }
  };

  return (
    <div>
      <div>
        <main role="main">
          <section className="jumbotron text-center bg-white">
            <div className="container">
              <i><h1 className="display-2">
                Friends TV Show API
              </h1>
              <nav>
              <Link to="/">Home</Link> |{" "}
            </nav>
              </i>
            </div>
          </section>
          <div className="album py-5" className="defaultColor text-white">
            <div className="container p-3">
              <div className="row">
              {friends.map(friend => {
              return (
              <div classname="col-md-6 p-0" key="{friend.id}" style={{backgroundColor: "transparent"}}>
              <div className="card mb-3 mx-2" style={{maxWidth: 540, backgroundColor: "#3C3E42"}}>
              <div className="row no-gutters">
                <div className="col-md-4">
                  <img src={friend.image} className="card-img" alt="..." />
                </div>
                <div className="col-md-8" style={{backgroundColor: "#3C3E42"}}>
                  <div className="card-body">
                    <h3 className="card-title">{friend.name}</h3>
                    <p><strong>”{friend.most_used_word}”</strong></p>
                    <p>Nickname : {friend.nickname}</p>
                    <p className="card-text">Portrayed By : {friend.portrayed_by}</p>
                    {/*
                    {  
                    friend.quotes.length > 0 &&            
                    <iframe width="560" height="315" src={`https://www.youtube.com/embed/${refactor(friend.quotes.length > 0 ? friend.quotes[0].video : null)}`} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    }
                    */}
                    <p className="card-text">Quotes : 
                    <Link to={{ pathname: `detail/${friend.id}`}}> Go to Quotes</Link>
                    </p>
                  </div>
                </div>
              </div>
              </div>
              </div>
              )})}
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
