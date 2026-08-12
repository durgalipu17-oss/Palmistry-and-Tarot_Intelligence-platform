import "./DashboardHome.css"; 
function DashboardHome() { 
    return ( 
        <div className="dashboard-home"> 
            <h1>✨ Welcome Back</h1> 
            <p>Your AI-powered Palmistry & Tarot dashboard</p> 
            <div className="card-grid"> 
                <div className="glass-card"> 
                    <h2>✋ Palm Analysis</h2> 
                    <p>Upload your palm and receive AI-powered insights.</p> 
                </div> 
                <div className="glass-card"> 
                    <h2>🃏 Tarot Reading</h2> 
                    <p>Draw tarot cards and get spiritual guidance.</p> 
                    </div> 
                    
                    <div className="glass-card"> 
                        <h2>📜 Reading History</h2> 
                        <p>Access all your previous palm and tarot readings.</p> 
                        </div> 
                        
                    </div> 
                </div> 
            ); 
    } 
export default DashboardHome;