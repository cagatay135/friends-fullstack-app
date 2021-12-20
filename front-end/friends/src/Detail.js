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
    const data = axios.get("http://127.0.0.1:8000/character/"+id).then((res) => {
      setFriends(res.data)
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
              <Link to="/">Home</Link>
            </nav>
              </i>
              <ul>
                
              </ul>
            </div>
          </section>
          
        </main>
        <div className="container-fluid">
  <div className="row p-5" style={{backgroundColor:"#3C3E42"}}>
    <div className="col-md-6 p-0">
  {                 
      
                            <div>
                                <h1 className="text-center text-white mb-0" style={{backgroundColor: friends.name=='Rachel Green' ? "#ED1F1F": friends.name=='Ross Geller' ? "#ED1F1F" : friends.name=='Monica Geller' ? "#02B2E8" : friends.name=='Chandler Bing' ? "#02B2E8" : friends.name=="Joey Tribbiani" ? "#FABC11" : "#FABC11"}}>
                                 {friends.name} 
                                 </h1>
                                <img src={friends.image} alt={friends.name} className="mt-0 w-100"/>
                            </div>
            }
            </div>
            <div className="col-md-6 overflow-auto h-50">
                            <div>
                                {
                                    friends.quotes &&
                                    friends.quotes.map(quote => {
                                        return (
                                            quote.video !== null &&
                                            <div key={quote.id} className="mb-4">
                                               <h4 className="text-white text-center">{quote.text}</h4>
                                                <iframe width="560" height="315" src={`https://www.youtube.com/embed/${refactor(quote.video)}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>                                            
                                            </div>
                                        )
                                    })
                                }
                            </div>
            </div>
  </div>
</div>
      </div>
      
  );
}

export default App;
