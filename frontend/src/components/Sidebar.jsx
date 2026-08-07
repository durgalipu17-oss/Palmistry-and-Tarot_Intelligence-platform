import "./Sidebar.css";

function Sidebar({activePage,setActivePage}){

    return(

        <div className="sidebar">

            <h2>🔮 Palmistry</h2>

            <button onClick={()=>setActivePage("dashboard")}>
                🏠 Dashboard
            </button>

            <button onClick={()=>setActivePage("palm")}>
                ✋ Palm Reading
            </button>

            <button onClick={()=>setActivePage("tarot")}>
                🃏 Tarot Reading
            </button>

            <button onClick={()=>setActivePage("history")}>
                📜 Reading History
            </button>

            <button onClick={()=>setActivePage("profile")}>
                👤 Profile
            </button>

            <button>
                🚪 Logout
            </button>

        </div>

    );

}

export default Sidebar;