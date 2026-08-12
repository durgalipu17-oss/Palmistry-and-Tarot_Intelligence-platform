import { useEffect, useState } from "react";
import api from "../api/api";
import "./Profile.css";

function Profile() {
  const [profile, setProfile] = useState({
    username: "",
    email: "",
    age: "",
    zodiac: "",
    interests: "",
    bio: ""
  });

  const [loading, setLoading] = useState(false);

//   useEffect(() => { 
//     const fetchProfile = async () => { 
//         try { 
//             const response = await api.get("/profile"); 
//             setProfile(response.data); 
//         } catch (err) { 
//             console.log(err); 
//         } 
//     }; 
//     fetchProfile(); 
// }, []);
  useEffect(() => { 
    const fetchProfile = async () => { 
        try { 
            const response = await api.get("/profile"); 
            console.log("Fetched profile:", response.data); 
            setProfile({ 
                username: response.data.username ?? "", 
                email: response.data.email ?? "", age: response.data.age ?? "", 
                zodiac: response.data.zodiac ?? "", 
                interests: response.data.interests ?? "", 
                bio: response.data.bio ?? "",
                // occupation: response.data.occupation ?? "", 
                // goals: response.data.goals ?? "",
                // reading_style: response.data.reading_style ?? "",
            }); 
            } catch (err) { 
                console.log(err);
             } }; 
             fetchProfile(); 
            }, []);

  const fetchProfile = async () => {
    try {
      const res = await api.get("/profile");
      setProfile(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value
    });
  };


    const handleSave = async () => {
  try {
    setLoading(true);

    const response = await api.put("/profile", {
      username: profile.username,
      email: profile.email,
      age: profile.age ? Number(profile.age) : null,
      zodiac: profile.zodiac || null,
      interests: profile.interests || null,
      bio: profile.bio || null,
    //   occupation: profile.occupation || null,
    //   goals: profile.goals || null,
    //   reading_style: profile.reading_style || null,
    });
     
    setProfile({ 
        username: response.data.username ?? "", 
        email: response.data.email ?? "", 
        age: response.data.age ?? "", 
        zodiac: response.data.zodiac ?? "", 
        interests: response.data.interests ?? "", 
        bio: response.data.bio ?? "", 
        // occupation: response.data.occupation ?? "", 
        // goals: response.data.goals ?? "", 
        // reading_style: response.data.reading_style ?? "",
        });

    

    alert("Profile updated successfully!");
  } catch (err) {
    console.log(err.response?.data || err);
    alert("Failed to update profile");
  } finally {
    setLoading(false);
  }
};
  return (
    <div className="profile-page">
      <h1>👤 My Profile</h1>

      <div className="profile-card">
        <label>Username</label>
        <input value={profile.username} disabled />

        <label>Email</label>
        <input value={profile.email} disabled />

        <label>Age</label>
        <input
          type="number"
          name="age"
          value={profile.age || ""}
          onChange={handleChange}
        />

        <label>Zodiac</label>
        <select
          name="zodiac"
          value={profile.zodiac || ""}
          onChange={handleChange}
        >
          <option value="">Select Zodiac</option>
          <option value="Aries">Aries</option>
          <option value="Taurus">Taurus</option>
          <option value="Gemini">Gemini</option>
          <option value="Cancer">Cancer</option>
          <option value="Leo">Leo</option>
          <option value="Virgo">Virgo</option>
          <option value="Libra">Libra</option>
          <option value="Scorpio">Scorpio</option>
          <option value="Sagittarius">Sagittarius</option>
          <option value="Capricorn">Capricorn</option>
          <option value="Aquarius">Aquarius</option>
          <option value="Pisces">Pisces</option>
        </select>

        <label>Interests</label>
        <input
          name="interests"
          value={profile.interests || ""}
          onChange={handleChange}
          placeholder="AI, Coding, Robotics..."
        />

        <label>Bio</label>
        <textarea
          name="bio"
          value={profile.bio || ""}
          onChange={handleChange}
          rows="4"
          placeholder="Tell something about yourself..."
        />

        <button className="save-btn" onClick={handleSave}>
          {loading ? "Saving..." : "💾 Save Changes"}
        </button>
      </div>
    </div>
  );
}

export default Profile;