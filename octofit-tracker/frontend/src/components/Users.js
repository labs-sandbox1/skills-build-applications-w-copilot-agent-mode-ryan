import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Users API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Users - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users - Processed data:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Users - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-2">Loading users...</p></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2><i className="bi bi-person-circle"></i> Users</h2>
      {users.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No users found.
        </div>
      ) : (
        <div className="row">
          {users.map((user) => (
            <div key={user.id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-header bg-success text-white">
                  <h5 className="card-title mb-0"><i className="bi bi-person"></i> {user.username}</h5>
                </div>
                <div className="card-body">
                  <ul className="list-group list-group-flush">
                    {user.email && (
                      <li className="list-group-item">
                        <i className="bi bi-envelope"></i> {user.email}
                      </li>
                    )}
                    {user.first_name && (
                      <li className="list-group-item">
                        <i className="bi bi-person-badge"></i> {user.first_name} {user.last_name}
                      </li>
                    )}
                    <li className="list-group-item">
                      <i className="bi bi-calendar-check"></i> Joined: {user.date_joined ? new Date(user.date_joined).toLocaleDateString() : 'N/A'}
                    </li>
                  </ul>
                </div>
                <div className="card-footer">
                  <button className="btn btn-success btn-sm w-100">View Profile</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Users;
