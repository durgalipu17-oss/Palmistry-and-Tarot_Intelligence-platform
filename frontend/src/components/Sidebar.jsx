import { useState } from "react";
import "./Sidebar.css";
function Sidebar({activePage,setActivePage}){
    const [menuOpen, setMenuOpen] = useState(false);
    const handleLogout = () => { 
        const confirmLogout = window.confirm( 
            "Are you sure you want to logout?" 
        ); 
        if (confirmLogout) { 
            localStorage.removeItem("token"); 
            window.location.href = "/"; 
        } 
    };
    return(
    <>
        <button
            className="mobile-menu-btn"
            onClick={() => setMenuOpen(!menuOpen)}
        >
            ☰
        </button>
        <div className={`sidebar ${menuOpen ? "sidebar-open" : ""}`}>
            <h2>🔮 Palmistry</h2>
            <button onClick={() => {
                setActivePage("dashboard");
                setMenuOpen(false);
            }}>
                🏠 Dashboard
            </button>
            <button onClick={() => {
                setActivePage("palm");
                setMenuOpen(false);
            }}>
                ✋ Palm Reading
            </button>
            <button onClick={()=> {
                setActivePage("tarot");
                setMenuOpen(false);
            }}>
                🃏 Tarot Reading
            </button>
            <button onClick={()=> {
                setActivePage("history");
                setMenuOpen(false);
            }}>
                📜 Reading History
            </button>
            <button onClick={()=> {
                setActivePage("profile");
                setMenuOpen(false);
            }}>
                👤 Profile
            </button>
            <button onClick={handleLogout}> 
                🚪 Logout 
            </button>
        </div>
        </>
    );
}
export default Sidebar;