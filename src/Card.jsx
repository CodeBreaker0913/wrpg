import profilePic from "./assets/Luffy Profile Pic.jpeg"

function Card(props) {
  return (
    <div className="card">
        <img className="card-image" src={profilePic} alt="Profile Picture"></img>
        <h2 className="card-title">{props.name}</h2>
        <p className="card-text">{props.text}</p>
    </div>
  );
}

export default Card
