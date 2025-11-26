import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-2">Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger" role="alert"><strong>Error:</strong> {error}</div></div>;

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'easy': 'bg-success',
      'medium': 'bg-warning text-dark',
      'hard': 'bg-danger'
    };
    return badges[difficulty?.toLowerCase()] || 'bg-secondary';
  };

  return (
    <div className="container mt-4">
      <h2><i className="bi bi-lightning"></i> Workout Suggestions</h2>
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No workout suggestions found.
        </div>
      ) : (
        <div className="row">
          {workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card h-100">
                <div className="card-header bg-warning text-dark">
                  <h5 className="card-title mb-0"><i className="bi bi-star-fill"></i> {workout.name || workout.title}</h5>
                </div>
                <div className="card-body">
                  {workout.description && (
                    <p className="card-text text-muted mb-3">{workout.description}</p>
                  )}
                  <ul className="list-group list-group-flush">
                    {workout.duration && (
                      <li className="list-group-item d-flex justify-content-between align-items-center">
                        <span><i className="bi bi-clock"></i> Duration</span>
                        <span className="badge bg-info">{workout.duration} min</span>
                      </li>
                    )}
                    {workout.difficulty && (
                      <li className="list-group-item d-flex justify-content-between align-items-center">
                        <span><i className="bi bi-speedometer"></i> Difficulty</span>
                        <span className={`badge ${getDifficultyBadge(workout.difficulty)}`}>{workout.difficulty}</span>
                      </li>
                    )}
                    {workout.category && (
                      <li className="list-group-item d-flex justify-content-between align-items-center">
                        <span><i className="bi bi-tag"></i> Category</span>
                        <span className="badge bg-primary">{workout.category}</span>
                      </li>
                    )}
                  </ul>
                </div>
                <div className="card-footer">
                  <button className="btn btn-warning w-100">Start Workout</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Workouts;
