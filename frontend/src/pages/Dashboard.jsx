import { useState } from "react";
import Sidebar from "../components/Sidebar";
import DashboardHome from "../components/DashboardHome";
import PalmReading from "../components/PalmReading";
import TarotReading from "../components/TarotReading";
import ReadingHistory from "../components/ReadingHistory";
import Profile from "../components/Profile";

import "./Dashboard.css";

function Dashboard() {

    const [activePage, setActivePage] = useState("dashboard");

    const renderContent = () => {

        switch (activePage) {

            case "dashboard":
                return <DashboardHome />;

            case "palm":
                return <PalmReading />;

            case "tarot":
                return <TarotReading />;

            case "history":
                return <ReadingHistory />;

            case "profile":
                return <Profile />;

            default:
                return <DashboardHome />;
        }
    };

    return (

        <div className="dashboard">

            <Sidebar
                activePage={activePage}
                setActivePage={setActivePage}
            />
            <div className="dashboard-content">
                {renderContent()}
            </div>
        </div>
    );
}

export default Dashboard;