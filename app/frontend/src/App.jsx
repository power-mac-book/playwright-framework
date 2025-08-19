import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import TestManager from "./pages/TestManager";
import TestDesignerPage from "./pages/TestDesignerPage";

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100 flex">
        {/* Sidebar */}
        <aside className="w-64 bg-gray-800 text-white p-4">
          <h1 className="text-2xl font-bold mb-6">Test Management</h1>
          <nav className="flex flex-col gap-3">
            <Link to="/" className="hover:bg-gray-700 p-2 rounded">Dashboard</Link>
            <Link to="/tests" className="hover:bg-gray-700 p-2 rounded">Manage Tests</Link>
            <Link to="/testdesigner" className="hover:bg-gray-700 p-2 rounded">Tests Designer</Link>
          </nav>
        </aside>

        {/* Content */}
        <main className="flex-1 p-6">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/tests" element={<TestManager />} />
            <Route path="/testdesigner" element={<TestDesignerPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}
