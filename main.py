import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "@/context/AuthContext";
import { ToastProvider } from "@/context/ToastContext";
import AppShell from "@/components/AppShell";
import Login from "@/pages/Login";
import Dashboard from "@/pages/Dashboard";
import DemandForecast from "@/pages/DemandForecast";
import Inventory from "@/pages/Inventory";
import Agents from "@/pages/Agents";
import Recommendations from "@/pages/Recommendations";
import Approval from "@/pages/Approval";
import Reports from "@/pages/Reports";
import type { JSX } from "react";

function Protected({ children }: { children: JSX.Element }) {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  return children;
}

function PublicOnly({ children }: { children: JSX.Element }) {
  const { user } = useAuth();
  if (user) return <Navigate to="/dashboard" replace />;
  return children;
}

export default function App() {
  return (
    <AuthProvider>
      <ToastProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<PublicOnly><Login /></PublicOnly>} />
            <Route
              element={
                <Protected>
                  <AppShell />
                </Protected>
              }
            >
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/forecast" element={<DemandForecast />} />
              <Route path="/inventory" element={<Inventory />} />
              <Route path="/agents" element={<Agents />} />
              <Route path="/recommendations" element={<Recommendations />} />
              <Route path="/approval" element={<Approval />} />
              <Route path="/reports" element={<Reports />} />
            </Route>
            <Route path="*" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </BrowserRouter>
      </ToastProvider>
    </AuthProvider>
  );
}
