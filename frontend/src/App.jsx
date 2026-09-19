import { useState } from "react";
import API from "./services/api";
import "./App.css";

function App() {
  const [query, setQuery] = useState(
    "SELECT * FROM PATIENT;"
  );

  const [columns, setColumns] = useState([]);
  const [rows, setRows] = useState([]);

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const [loading, setLoading] = useState(false);

  const [showPasskey, setShowPasskey] = useState(false);
  const [passkey, setPasskey] = useState("");

  // ==========================================================
  // CHECK WHETHER QUERY NEEDS PASSKEY
  // ==========================================================

  const needsPasskey = () => {
    const command = query
      .trim()
      .split(/\s+/)[0]
      ?.toLowerCase();

    const protectedCommands = [
      "insert",
      "update",
      "delete",
      "create",
      "alter",
      "drop",
      "truncate",
      "replace",
    ];

    return protectedCommands.includes(command);
  };

  // ==========================================================
  // EXECUTE QUERY BUTTON
  // ==========================================================

  const executeQuery = () => {
    if (!query.trim()) {
      setError("Please enter a SQL query.");
      setMessage("");
      return;
    }

    setError("");
    setMessage("");

    setColumns([]);
    setRows([]);

    // Protected query → show passkey popup
    if (needsPasskey()) {
      // Always clear old passkey
      setPasskey("");

      setShowPasskey(true);

      return;
    }

    // Normal query
    runQuery("");
  };

  // ==========================================================
  // SEND QUERY TO DJANGO
  // ==========================================================

  const runQuery = async (enteredPasskey) => {
    setLoading(true);

    setError("");
    setMessage("");

    setColumns([]);
    setRows([]);

    try {
      const response = await API.post(
        "query/",
        {
          query: query,
          passkey: enteredPasskey,
        }
      );

      setColumns(
        response.data.columns || []
      );

      setRows(
        response.data.rows || []
      );

      setMessage(
        response.data.message || ""
      );

    } catch (err) {
      setError(
        err.response?.data?.error ||
        "Unable to execute the SQL query."
      );

    } finally {
      // Always clear passkey
      setPasskey("");

      // Always close popup
      setShowPasskey(false);

      setLoading(false);
    }
  };

  // ==========================================================
  // CANCEL PASSKEY
  // ==========================================================

  const cancelPasskey = () => {
    setShowPasskey(false);
    setPasskey("");
  };

  // ==========================================================
  // JSX
  // ==========================================================

  return (
    <div className="hospital-app">

      {/* ====================================================
          HEADER
      ==================================================== */}

      <header className="hospital-header">

        <div className="hospital-brand">

          <div className="hospital-logo">
            <i class="bi bi-heart-pulse"></i>
          </div>

          <div>
            <h1>
              Hospital Management System
            </h1>

            <p>
              Database Management Portal
            </p>
          </div>

        </div>

        <div className="database-status">
          <span></span>
          SQLite Connected
        </div>

      </header>


      {/* ====================================================
          MAIN
      ==================================================== */}

      <main className="hospital-main">

        {/* ==================================================
            TITLE
        ================================================== */}

        <div className="welcome-section">

          <div className="medical-symbol">
            <i class="bi bi-heart-pulse"></i>
          </div>

          <div>

            <h2>
              SQL Query Console
            </h2>

            <p>
              Execute SQL queries and manage
              hospital database records.
            </p>

          </div>

        </div>


        {/* ==================================================
            SQL SECTION
        ================================================== */}

        <section className="sql-section">

          <div className="section-title">

            <div>

              <h3>
                SQL Query
              </h3>

              <p>
                Enter your SQL statement below
              </p>

            </div>

            <div className="sql-badge">
              SQL
            </div>

          </div>


          {/* =================================================
              EDITOR
          ================================================= */}

          <div className="sql-editor">

            <div className="editor-top">

              <span className="editor-dot"></span>

              <span className="editor-dot"></span>

              <span className="editor-dot"></span>

              <span className="editor-name">
                query.sql
              </span>

            </div>


            <div className="editor-body">

              <div className="line-number">
                1
              </div>

              <textarea
                value={query}
                onChange={(e) =>
                  setQuery(e.target.value)
                }
                spellCheck="false"
                placeholder="Write your SQL query here..."
              />

            </div>

          </div>


          {/* =================================================
              ACTIONS
          ================================================= */}

          <div className="query-actions">

            <div className="query-help">

              <span>
                SELECT
              </span>

              <span>
                INSERT
              </span>

              <span>
                UPDATE
              </span>

              <span>
                DELETE
              </span>

              <span>
                CREATE
              </span>

              <span>
                ALTER
              </span>

              <span>
                DROP
              </span>

            </div>


            <button
              className="run-button"
              onClick={executeQuery}
              disabled={loading}
            >

              {loading ? (

                <>
                  <span className="spinner"></span>
                  Executing...
                </>

              ) : (

                <>
                  <span>
                    ▶
                  </span>

                  Execute Query
                </>

              )}

            </button>

          </div>

        </section>


        {/* ==================================================
            SUCCESS MESSAGE
        ================================================== */}

        {message && (

          <div className="success-message">

            <div className="success-icon">
              ✓
            </div>

            <div>

              <strong>
                Query Executed Successfully
              </strong>

              <p>
                {message}
              </p>

            </div>

          </div>

        )}


        {/* ==================================================
            ERROR MESSAGE
        ================================================== */}

        {error && (

          <div className="error-message">

            <div className="error-icon">
              !
            </div>

            <div>

              <strong>
                Query Execution Failed
              </strong>

              <p>
                {error}
              </p>

            </div>

          </div>

        )}


        {/* ==================================================
            RESULTS
        ================================================== */}

        {columns.length > 0 && (

          <section className="results-section">

            <div className="results-title">

              <div>

                <span>
                  DATABASE RESULT
                </span>

                <h3>
                  Query Results
                </h3>

              </div>

              <div className="record-count">

                {rows.length}

                {" "}

                {rows.length === 1
                  ? "Record"
                  : "Records"}

              </div>

            </div>


            <div className="table-wrapper">

              <table>

                <thead>

                  <tr>

                    {columns.map(
                      (column) => (

                        <th key={column}>
                          {column}
                        </th>

                      )
                    )}

                  </tr>

                </thead>


                <tbody>

                  {rows.map(
                    (row, rowIndex) => (

                      <tr key={rowIndex}>

                        {columns.map(
                          (column, columnIndex) => (

                            <td key={columnIndex}>

                              {row[columnIndex] ?? "—"}

                            </td>

                          )
                        )}

                      </tr>

                    )
                  )}

                </tbody>

              </table>


              {rows.length === 0 && (

                <div className="no-results">

                  Query executed successfully,
                  but no records were found.

                </div>

              )}

            </div>

          </section>

        )}

      </main>


      {/* ====================================================
          FOOTER
      ==================================================== */}

      <footer className="hospital-footer">

        Hospital Management System

        <span>
          •
        </span>

        Database Query Console

      </footer>


      {/* ====================================================
          PASSKEY POPUP
      ==================================================== */}

      {showPasskey && (

        <div className="passkey-overlay">

          <div className="passkey-modal">

            <div className="passkey-icon">
              🔐
            </div>

            <h3>
              Passkey Required
            </h3>

            <p>
              This SQL query can modify
              the hospital database.

              <br />

              Enter the passkey to continue.
            </p>


            <input
              type="password"
              value={passkey}
              onChange={(e) =>
                setPasskey(e.target.value)
              }
              placeholder="Enter passkey"
              autoFocus
              onKeyDown={(e) => {

                if (
                  e.key === "Enter" &&
                  passkey
                ) {
                  runQuery(passkey);
                }

              }}
            />


            <div className="passkey-actions">

              <button
                className="cancel-button"
                onClick={cancelPasskey}
                disabled={loading}
              >
                Cancel
              </button>


              <button
                className="confirm-button"
                onClick={() =>
                  runQuery(passkey)
                }
                disabled={
                  !passkey || loading
                }
              >

                {loading
                  ? "Checking..."
                  : "Confirm"}

              </button>

            </div>

          </div>

        </div>

      )}

    </div>
  );
}

export default App;
