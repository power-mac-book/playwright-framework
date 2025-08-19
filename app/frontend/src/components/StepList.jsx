import TestStep from './TestStep';

export default function StepList({ steps, updateStep, removeStep, addStep }) {
  return (
    <div>
      {steps.map((step, idx) => (
        <TestStep key={idx} step={step} index={idx} updateStep={updateStep} removeStep={removeStep} />
      ))}
      <button className="bg-blue-500 text-white px-4 py-2 mt-2" onClick={addStep}>Add Step</button>
    </div>
  );
}
