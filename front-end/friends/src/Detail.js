import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import { Link, useParams } from "react-router-dom";

function App() {
  const [friends, setFriends] = useState([]);
  useEffect(() => {
    //axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
    //axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    const data = axios.get("http://localhost:8000/1",{headers : {'Content-Type':'application/json;charset=utf-8','Access-Control-Allow-Origin':'*'}}).then((res) => {
      setFriends(res.data);
    });
  }, []);
  let { id } = useParams();

  console.log(id)

  const refactor = (url) => {
    if (url !== null) {
      let new_url = url.replace(/^(?:https?:\/\/)?(?:www\.)?/i, "");
      new_url = new_url.split("=")[1];
      return new_url;
    }
  };

  return (
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
          
        </main>
        <div class="container-fluid">
  <div class="row p-5" style={{backgroundColor:"#3C3E42"}}>
    <div class="col-md-6 p-0">
  {                 
                friends.map(friend => {
                    if(friend.id == id){
                        return (
                            <div key={friend.id}>
                                <h1 className="text-center text-white mb-0" style={{backgroundColor: friend.name=='Rachel Green' ? "#ED1F1F": friend.name=='Ross Geller' ? "#ED1F1F" : friend.name=='Monica Geller' ? "#02B2E8" : friend.name=='Chandler Bing' ? "#02B2E8" : friend.name=="Joey Tribbiani" ? "#FABC11" : "#FABC11"}}>
                                 {friend.name} 
                                 </h1>
                                <img src={friend.image} alt={friend.name} className="mt-0 w-100"/>
                            </div>
                        )
                    }
                }
                )
            }
            </div>
            <div className="col-md-6">
            {
                friends.map(friend => {
                    if(friend.id == id){
                        return (
                            <div key={friend.id}>
                                {
                                    friend.quotes.length > 0 &&
                                    friend.quotes.map(quote => {
                                        return (
                                            quote.video !== null &&
                                            <div key={quote.id} className="mb-4">
                                               <h4 className="text-white text-center">{quote.text}</h4>
                                                <iframe width="560" height="315" src={`https://www.youtube.com/embed/${refactor(quote.video)}`} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>                                            
                                            </div>
                                        )
                                    })
                                }
                            </div>
                        )
                    }
                }
                )
             }
            </div>
  </div>
</div>
      </div>
      
  );
}

export default App;
